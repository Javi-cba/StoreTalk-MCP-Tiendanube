import { esUY } from "@clerk/localizations";

/** Después de loguearse va a sus tiendas (sin tiendas, ahí mismo está el botón para conectar). */
export const AFTER_AUTH_URL = "/dashboard";

/** Login/registro propios: sin esto, con claves de producción Clerk manda al Account Portal
 * (accounts.<dominio>), que no existe en *.amplifyapp.com. */
export const SIGN_IN_URL = "/sign-in";
export const SIGN_UP_URL = "/sign-up";

export const clerkLocalization = esUY;

/** Componentes de Clerk que quedan (menú de cuenta) con los colores de la marca. */
export const clerkAppearance = {
  variables: {
    colorPrimary: "#2563eb",
    borderRadius: "0.875rem",
    fontFamily: "var(--font-geist-sans), sans-serif",
  },
};
