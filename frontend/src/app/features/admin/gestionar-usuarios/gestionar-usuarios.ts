import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-usuarios',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-usuarios.html',
  styleUrl: './gestionar-usuarios.scss',
})
export class GestionarUsuarios implements OnInit {
  usuarioForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.usuarioForm = this.fb.group({
      buscar: [''],
      email: ['', [Validators.required, Validators.email]],
      contrasena: ['', [Validators.required]],
      idTipoUsuario: ['1', [Validators.required]], // 1 = Admin, 2 = Pasajero
    });
  }

  onSubmit(): void {
    if (this.usuarioForm.valid) {
      console.log('Usuario guardado:', this.usuarioForm.value);
    }
  }

  onEliminar(): void {
    console.log('Eliminando usuario...');
  }
}
