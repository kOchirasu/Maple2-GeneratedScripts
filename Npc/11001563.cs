using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001563: Ishura
/// </summary>
public class _11001563 : NpcScript {
    internal _11001563(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006051$ 
                // - You're here.
                return true;
            case 10:
                // $script:0515180307006106$ 
                // - $MyPCName$, $npcName:11001232[gender:1]$ says she misses you. 
                // $script:0515180307006107$ 
                // - I'm sorry I didn't stay in touch. I couldn't find the time. Still, it seems you did well enough without me.
                return true;
            default:
                return true;
        }
    }
}
