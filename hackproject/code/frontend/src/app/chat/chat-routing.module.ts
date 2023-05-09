import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AxaLayoutComponent } from '../shared/axa-layout/axa-layout.component';
import {ChatHomeComponent} from "./chat-home/chat-home.component";

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'home',
        component: ChatHomeComponent
      },
      {
        path: 'axa',
        component: AxaLayoutComponent
      }
    ],
  },
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ChatRoutingModule { }
