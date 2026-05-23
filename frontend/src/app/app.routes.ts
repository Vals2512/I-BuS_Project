import { Routes } from '@angular/router';
import { LoginComponent } from './features/auth/login/login';
import { RegistroComponent } from './features/auth/registro/registro';
import { PerfilComponent } from './features/auth/perfil/perfil';
import { Dashboard as AdminDashboard } from './features/admin/dashboard/dashboard';
import { Estadisticas } from './features/admin/estadisticas/estadisticas';
import { GestionarBarrios } from './features/admin/gestionar-barrios/gestionar-barrios';
import { GestionarEmpresas } from './features/admin/gestionar-empresas/gestionar-empresas';
import { GestionarRutas } from './features/admin/gestionar-rutas/gestionar-rutas';
import { Dashboard as UsuarioDashboard } from './features/usuario/dashboard/dashboard';
import { BuscarRutas } from './features/usuario/buscar-rutas/buscar-rutas';

export const routes: Routes = [
    { path: '', redirectTo: 'auth/login', pathMatch: 'full' },
    { path: 'auth/login', component: LoginComponent },
    { path: 'auth/registro', component: RegistroComponent },
    { path: 'auth/perfil', component: PerfilComponent },
    { path: 'admin/dashboard', component: AdminDashboard },
    { path: 'admin/estadisticas', component: Estadisticas },
    { path: 'admin/barrios', component: GestionarBarrios },
    { path: 'admin/empresas', component: GestionarEmpresas },
    { path: 'admin/rutas', component: GestionarRutas },
    { path: 'usuario/dashboard', component: UsuarioDashboard },
    { path: 'usuario/buscar-rutas', component: BuscarRutas },
    { path: '**', redirectTo: 'auth/login' }
];