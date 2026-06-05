import AuthGuard from "@/components/auth/AuthGuard";
import DashboardLayout from "@/components/layouts/DashboardLayout";
import DashboardGrid from "@/components/dashboard/DashboardGrid";

export default function DashboardPage() {
  return (
    <AuthGuard>
      <DashboardLayout>
        <DashboardGrid />
      </DashboardLayout>
    </AuthGuard>
  );
}
