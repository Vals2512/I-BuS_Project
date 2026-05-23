import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionarBarrios } from './gestionar-barrios';

describe('GestionarBarrios', () => {
  let component: GestionarBarrios;
  let fixture: ComponentFixture<GestionarBarrios>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GestionarBarrios],
    }).compileComponents();

    fixture = TestBed.createComponent(GestionarBarrios);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
