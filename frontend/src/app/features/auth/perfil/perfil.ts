import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.html',
  imports: [ReactiveFormsModule, RouterModule]
})
export class PerfilComponent implements OnInit {
  perfilForm!: FormGroup;

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
    // Aquí puedes limpiar tokens de localStorage si existieran
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