using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000565: Porte
/// </summary>
public class _11000565 : NpcScript {
    internal _11000565(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002339$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407002341$ 
                // - I have the ability to meld with the darkness. What can you do?
                return true;
            default:
                return true;
        }
    }
}
