import { Routes } from '@angular/router';
import { LoginComponent } from './features/auth/login/login';
import { RegistroComponent } from './features/auth/registro/registro';
import { PerfilComponent } from './features/auth/perfil/perfil';
import { Dashboard as AdminDashboard } from './features/admin/dashboard/dashboard';
import { Estadisticas } from './features/admin/estadisticas/estadisticas';
import { GestionarBarrios } from './features/admin/gestionar-barrios/gestionar-barrios';
import { GestionarEmpresas } from './features/admin/gestionar-empresas/gestionar-empresas';
import { GestionarRutas } from './features/admin/gestionar-rutas/gestionar-rutas';
import { GestionarUsuarios } from './features/admin/gestionar-usuarios/gestionar-usuarios';
import { BuscarRutas } from './features/usuario/buscar-rutas/buscar-rutas';
import { PanelAjustes } from './features/ajustes/panel-ajustes/panel-ajustes';
import { GestionarDetalleRuta } from './features/admin/gestionar-rutas/components/gestionar-detalle-ruta/gestionar-detalle-ruta';
import { GestionarHorarios } from './features/admin/gestionar-rutas/components/gestionar-horarios/gestionar-horarios';
import { GestionarTiempos } from './features/admin/gestionar-rutas/components/gestionar-tiempos/gestionar-tiempos';

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
    { path: 'admin/rutas/detalle', component: GestionarDetalleRuta },
    { path: 'admin/rutas/horarios', component: GestionarHorarios },
    { path: 'admin/rutas/tiempos', component: GestionarTiempos },
    { path: 'admin/usuarios', component: GestionarUsuarios },
    { path: 'usuario/dashboard', redirectTo: 'usuario/buscar-rutas', pathMatch: 'full' },
    { path: 'usuario/buscar-rutas', component: BuscarRutas },
    { path: 'usuario/ajustes', component: PanelAjustes },
    { path: '**', redirectTo: 'auth/login' }
];