import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionarEmpresas } from './gestionar-empresas';

describe('GestionarEmpresas', () => {
  let component: GestionarEmpresas;
  let fixture: ComponentFixture<GestionarEmpresas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GestionarEmpresas],
    }).compileComponents();

    fixture = TestBed.createComponent(GestionarEmpresas);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
