import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-empresas',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-empresas.html',
  styleUrl: './gestionar-empresas.scss',
})
export class GestionarEmpresas implements OnInit {
  empresaForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.empresaForm = this.fb.group({
      buscar: [''],
      idEmpresa: ['E - 10'],
      nombreEmpresa: ['Cootradelsol'],
      nit: ['800.123.456-7'],
      telefono: ['3101234567'],
      direccion: ['Calle 10 # 5 - 20'],
    });
  }

  onSubmit(): void {
    console.log('Empresa editada:', this.empresaForm.value);
  }

  onEliminar(): void {
    console.log('Eliminando empresa...');
  }
}
