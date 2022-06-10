using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000222: Patrick
/// </summary>
public class _11000222 : NpcScript {
    internal _11000222(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000970$ 
                // - May I help you?
                return true;
            case 20:
                // $script:0831180407000972$ 
                // - I've got a daughter. She's the apple of my eye. Her name is $npcName:11000221[gender:1]$. She was the last gift my wife gave me before she passed away.
                return true;
            default:
                return true;
        }
    }
}
