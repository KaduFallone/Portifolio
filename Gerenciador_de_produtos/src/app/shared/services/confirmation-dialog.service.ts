import { Component, inject, Injectable } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-confirmatio-dialog',
  template: `
    <h2 mat-dialog-title>Delete produto</h2>
    <mat-dialog-content>
      Certeza de que deseja deletar este produto?
    </mat-dialog-content>
    <mat-dialog-actions align="start">
      <button mat-raised-button color="accent" (click)="onNo()">Não</button>
      <button mat-raised-button color="warn"(click)="onYes()" cdkFocusInitial>Sim</button>
    </mat-dialog-actions>
  `,
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
})
export class ConfirmationDialogComponent {
  matDialogRef = inject(MatDialogRef)

  onNo(){
    this.matDialogRef.close(false);
  }

  onYes(){
    this.matDialogRef.close(true)
  }
}

@Injectable({
  providedIn: 'root'
})
export class ConfirmationDialogService {

  matDialog = inject(MatDialog);

  constructor() { }

  openDialog(): Observable<boolean> {
        return this.matDialog
          .open(ConfirmationDialogComponent).afterClosed();
  };
}
