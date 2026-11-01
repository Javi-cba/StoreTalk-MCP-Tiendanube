import { ClerkProvider } from "@clerk/nextjs";
import { PageBackground } from "@/components/layout/page-background";
import { clerkAppearance, clerkLocalization, SIGN_IN_URL, SIGN_UP_URL } from "@/lib/auth/clerk";
import { clerkProxyUrl } from "@/lib/auth/clerkProxy";

/** Login y registro: pantalla completa, sin navbar ni footer (la vuelta del OAuth los agrega en su página). */
export default function AuthLayout({ children }: LayoutProps<"/">) {
  return (
    <ClerkProvider localization={clerkLocalization} appearance={clerkAppearance} proxyUrl={clerkProxyUrl}
      signInUrl={SIGN_IN_URL} signUpUrl={SIGN_UP_URL}>
      <PageBackground />
      <main className="flex flex-1 flex-col">{children}</main>
    </ClerkProvider>
  );
}
