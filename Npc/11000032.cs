using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000032: Einos
/// </summary>
public class _11000032 : NpcScript {
    internal _11000032(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000183$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000184$ 
                // - We should let $npcName:11000031[gender:0]$ know his identity and ask for advice. Meet me in $map:02000035$.
                return true;
            default:
                return true;
        }
    }
}
