# StoreTalk

Gestioná tu Tiendanube conversando con tu asistente de IA. Conectás tu tienda una vez y después le pedís en lenguaje natural lo que necesitás: *"subí 10% los precios de la categoría remeras"*, *"mostrame los pedidos de hoy"*, *"creá un cupón del 15% para el finde"*.

StoreTalk es un **servidor MCP remoto** (FastAPI + FastMCP) con un sitio web (Next.js) para registrarte, conectar tu tienda y vincular tu asistente (Claude web/desktop/celular, Claude Code, etc.).

## ✨ Qué podés hacer

- **Productos:** listar, ver, crear, editar y eliminar productos; subir o bajar precios por categoría en porcentaje, con vista previa antes de aplicar.
- **Variantes:** agregar, editar y eliminar variantes (talle, color) con su propio precio y stock.
- **Imágenes:** agregar, actualizar y eliminar imágenes de productos.
- **Categorías:** listar, crear, editar y eliminar categorías.
- **Pedidos:** listar y ver el detalle; cerrar, reabrir, cancelar y agregar notas.
- **Cupones:** listar, ver, crear, editar y eliminar cupones de descuento.

## 🔐 Cómo funciona

1. Te registrás en el sitio (Clerk).
2. Conectás tu Tiendanube con OAuth y ves los permisos otorgados.
3. Agregás StoreTalk como conector en tu asistente (`/mcp`), iniciás sesión, elegís la tienda y autorizás.
4. Empezás a conversar.

Los tokens de Tiendanube se guardan cifrados (AES-256-GCM), los datos de la tienda se consultan siempre en vivo y podés desconectar tu tienda desde el dashboard cuando quieras.

## 🧰 Stack

- **Backend:** Python 3.12, FastAPI, FastMCP (Streamable HTTP), SQLAlchemy + Alembic, Postgres (Neon).
- **Frontend:** Next.js (App Router), React, TypeScript, Tailwind, Clerk.
- **Cloud (AWS):** frontend en Amplify Hosting (SSR); backend como imagen Docker en ECR, corriendo en AWS Lambda (Lambda Web Adapter + Function URL). Primero lo desplegamos en ECS Fargate (Express Mode), y después lo pasamos a Lambda por costo: free tier.

## 🖥️ Levantarlo en local

Requisitos: [uv](https://docs.astral.sh/uv/), Node 20+, una base Postgres (Neon sirve), una app de Tiendanube Partners, una instancia de Clerk y [ngrok](https://ngrok.com/).

1. **Variables:** copiá `backend/.env.example` a `.env` en la raíz y `frontend/.env.example` a `frontend/.env.local`, y completalas (`ENCRYPTION_KEY` y `API_KEY_PEPPER` se generan con el comando que figura en el ejemplo).
2. **Túnel:** `ngrok http 8000`. Usá esa URL en `PUBLIC_BASE_URL` (`.env`), en `NEXT_PUBLIC_MCP_URL=<ngrok>/mcp` (`frontend/.env.local`) y como Redirect URL en Tiendanube Partners: `<ngrok>/api/tiendanube/callback`.
3. **Backend** (en `backend/`):
   ```bash
   uv sync
   uv run alembic upgrade head
   uv run uvicorn src.main:app --reload   # API en :8000, MCP en :8000/mcp
   ```
4. **Frontend** (en `frontend/`):
   ```bash
   npm install
   npm run dev                            # http://localhost:3000
   ```
5. Entrá a `http://localhost:3000`, conectá tu tienda y seguí la guía de `/connect-ai` para sumar el conector `<ngrok>/mcp` a tu asistente.

Más detalle (API keys manuales, MCP Inspector, tests) en [`backend/LOCAL_DEV.md`](backend/LOCAL_DEV.md).
