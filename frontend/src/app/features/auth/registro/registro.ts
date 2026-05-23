import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.html',
  standalone: true,
  imports: [ReactiveFormsModule, RouterModule]
})
export class RegistroComponent implements OnInit {
  registroForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
    this.registroForm = this.fb.group({
      nombre: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      terminos: [false, Validators.requiredTrue]
    });
  }

  onSubmit(): void {
    if (this.registroForm.valid) {
      console.log('Registro enviado:', this.registroForm.value);
      this.router.navigate(['/auth/login']);

      this.authService.register(this.registroForm.value).subscribe({
        next: (res) => {
          console.log('Registro exitoso (API)', res);
        },
        error: (err) => {
          console.warn('Error en el registro API (normal si el backend no está corriendo):', err);
        }
      });
    }
  }
}