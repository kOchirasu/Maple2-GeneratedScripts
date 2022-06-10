using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000135: Squattush
/// </summary>
public class _11000135 : NpcScript {
    internal _11000135(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000559$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407000561$ 
                // - Shush! Lower your voice.
                return true;
            default:
                return true;
        }
    }
}
