use bevy::prelude::*;
use crate::components::creature::Creature;

pub fn move_creatures(mut query: Query<(&Creature, &mut Transform)>) { 
    for (creature, mut transform) in query.iter_mut(){ 
        transform.translation.x += creature.speed;
    }
}