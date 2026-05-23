import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-horarios',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-horarios.html',
  styleUrl: './gestionar-horarios.scss',
})
export class GestionarHorarios implements OnInit {
  horarioForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.horarioForm = this.fb.group({
      buscar: [''],
      idEmpresa: ['1', [Validators.required]],
      horaSalida: ['05:00', [Validators.required]],
      horaLlegada: ['07:30', [Validators.required]],
    });
  }

  onSubmit(): void {
    if (this.horarioForm.valid) {
      console.log('Horario guardado:', this.horarioForm.value);
    }
  }

  onEliminar(): void {
    console.log('Eliminando horario...');
  }
}
