import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionarRutas } from './gestionar-rutas';

describe('GestionarRutas', () => {
  let component: GestionarRutas;
  let fixture: ComponentFixture<GestionarRutas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GestionarRutas],
    }).compileComponents();

    fixture = TestBed.createComponent(GestionarRutas);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
