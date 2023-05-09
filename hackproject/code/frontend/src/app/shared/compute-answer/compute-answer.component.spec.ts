import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComputeAnswerComponent } from './compute-answer.component';

describe('ComputeAnswerComponent', () => {
  let component: ComputeAnswerComponent;
  let fixture: ComponentFixture<ComputeAnswerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComputeAnswerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComputeAnswerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
