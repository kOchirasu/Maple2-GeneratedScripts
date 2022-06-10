using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004209: Humhum
/// </summary>
public class _11004209 : NpcScript {
    internal _11004209(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806045807010664$ 
                // - What is it?
                return true;
            case 10:
                // $script:0806045807010665$ 
                // - Hmm? Is that really the $npc:11004213[gender:0]$, you ask? Yep! Except this one is bigger. Otherwise, they're identical in every way! The real $npc:11004213[gender:0]$ is full of hot air, too, heh heh heh!
                return true;
            default:
                return true;
        }
    }
}
