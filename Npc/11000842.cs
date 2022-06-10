using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000842: Angela
/// </summary>
public class _11000842 : NpcScript {
    internal _11000842(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003080$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407003083$ 
                // - Ah, I don't care about justice or world peace. I just don't like it when people bully the weak. No one has the right to make others suffer, no matter how strong they are. 
                return true;
            default:
                return true;
        }
    }
}
