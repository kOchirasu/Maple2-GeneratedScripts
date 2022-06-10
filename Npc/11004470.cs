using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004470: Colorata
/// </summary>
public class _11004470 : NpcScript {
    internal _11004470(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227195007012417$ 
                // - I was playing hide-and-seek with my friends, but I just can't find them!
                return true;
            case 10:
                // $script:1227195007012418$ 
                // - I was playing hide-and-seek with my friends, but I just can't find them!
                // $script:1227195007012419$ 
                // - Where did you go?! I give up! Please come out!
                return true;
            default:
                return true;
        }
    }
}
