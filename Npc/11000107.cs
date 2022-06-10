using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000107: Lucy
/// </summary>
public class _11000107 : NpcScript {
    internal _11000107(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000438$ 
                // - What is it?
                return true;
            case 40:
                // $script:0831180407000441$ 
                // - The Royal Road is blocked, and the forest path is too dangerous. I can't even go back home since the sea routes are messed up now too. I don't know what to do.
                return true;
            default:
                return true;
        }
    }
}
