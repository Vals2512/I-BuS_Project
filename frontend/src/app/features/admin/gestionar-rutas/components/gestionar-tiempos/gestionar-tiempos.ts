import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-tiempos',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-tiempos.html',
  styleUrl: './gestionar-tiempos.scss',
})
export class GestionarTiempos implements OnInit {
  tiempoForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.tiempoForm = this.fb.group({
      buscar: [''],
      fecha: ['2026-05-23', [Validators.required]],
    });
  }

  onSubmit(): void {
    if (this.tiempoForm.valid) {
      console.log('Tiempo guardado:', this.tiempoForm.value);
    }
  }

  onEliminar(): void {
    console.log('Eliminando tiempo...');
  }
}
