import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.html',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule]
})
export class PerfilComponent implements OnInit {
  perfilForm!: FormGroup;

  favoritos = [
    { tipo: 'casa', nombre: 'Casa', direccion: 'Calle 10 # 5-20' },
    { tipo: 'trabajo', nombre: 'Trabajo', direccion: 'Avenida El Dorado # 60-15' },
    { tipo: 'trabajo', nombre: 'Universidad', direccion: 'Carrera 30 # 45-03' },
    { tipo: 'casa', nombre: 'Casa de Abuela', direccion: 'Transversal 5 # 78-12' }
  ];

  historial = [
    { ruta: 'Ruta 1 - Circular Norte', tiempo: 'Hace 5 min' },
    { ruta: 'Ruta 5 - Expreso Sur', tiempo: 'Ayer' },
    { ruta: 'Ruta 10 - Transversal', tiempo: 'Hace 3 días' },
    { ruta: 'Ruta 3 - Alimentador', tiempo: 'Hace 1 semana' }
  ];

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
    this.perfilForm = this.fb.group({
      email: ['usuario@ibus.com', [Validators.required, Validators.email]],
    });
  }

  onActualizar(): void {
    if (this.perfilForm.valid) {
      console.log('Actualizando cuenta...', this.perfilForm.value);
      this.authService.updateProfile(this.perfilForm.value).subscribe({
        next: (res) => console.log('Perfil actualizado', res),
        error: (err) => console.error('Error al actualizar perfil', err)
      });
    }
  }

  onCerrarSesion(): void {
    console.log('Cerrando sesión...');
    this.router.navigate(['/auth/login']);
  }

  onEliminarCuenta(): void {
    const confirmar = confirm('¿Estás seguro de que deseas eliminar tu cuenta? Esta acción no se puede deshacer.');
    if (confirmar) {
      console.log('Solicitud para eliminar cuenta enviada');
      this.authService.deleteAccount().subscribe({
        next: (res) => {
          console.log('Cuenta eliminada', res);
          this.router.navigate(['/auth/login']);
        },
        error: (err) => console.error('Error al eliminar cuenta', err)
      });
    }
  }
}