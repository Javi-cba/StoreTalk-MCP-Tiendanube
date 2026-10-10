/**
 * Producción sin dominio propio: `*.amplifyapp.com` no acepta los CNAME que pide Clerk
 * (clerk.<dominio>), así que su Frontend API se sirve desde esta misma app en /__clerk
 * (lo mismo que Clerk hace solo en *.vercel.app). Solo con claves de producción: en local,
 * con claves de desarrollo, Clerk funciona directo.
 * En el dashboard de Clerk: Domains → Proxy configuration → https://<dominio>/__clerk.
 */
export const CLERK_PROXY_PATH = "/__clerk";

export const clerkUsesProxy = process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY?.startsWith("pk_live_") ?? false;

/** `proxyUrl` para ClerkProvider (relativo: lo resuelve contra el dominio actual). */
export const clerkProxyUrl = clerkUsesProxy ? CLERK_PROXY_PATH : undefined;
