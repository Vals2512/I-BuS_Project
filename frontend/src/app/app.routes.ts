import { Routes } from '@angular/router';
import { LoginComponent } from './features/auth/login/login';
import { RegistroComponent } from './features/auth/registro/registro';
import { PerfilComponent } from './features/auth/perfil/perfil';

export const routes: Routes = [
    { path: '', redirectTo: 'auth/login', pathMatch: 'full' },
    { path: 'auth/login', component: LoginComponent },
    { path: 'auth/registro', component: RegistroComponent },
    { path: 'auth/perfil', component: PerfilComponent },
    { path: '**', redirectTo: 'auth/login' }
];