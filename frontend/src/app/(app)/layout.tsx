import { ClerkProvider } from "@clerk/nextjs";
import { Suspense } from "react";
import { Footer } from "@/components/layout/footer";
import { Navbar } from "@/components/layout/navbar";
import { PageBackground } from "@/components/layout/page-background";
import { AccountActions } from "@/components/layout/account-actions";
import { clerkAppearance, clerkLocalization, SIGN_IN_URL, SIGN_UP_URL } from "@/lib/auth/clerk";
import { clerkProxyUrl } from "@/lib/auth/clerkProxy";

/** Área privada: Clerk vive solo acá, la landing no lo carga. */
export default function AppLayout({ children }: LayoutProps<"/">) {
  return (
    <ClerkProvider localization={clerkLocalization} appearance={clerkAppearance} proxyUrl={clerkProxyUrl}
      signInUrl={SIGN_IN_URL} signUpUrl={SIGN_UP_URL}>
      <PageBackground />
      <Navbar intro={false} actions={
          <Suspense>
            <AccountActions />
          </Suspense>
        } />
      <main className="flex flex-1 flex-col pt-(--navbar-height)">{children}</main>
      <Footer />
    </ClerkProvider>
  );
}
