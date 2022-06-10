using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001304: Asimov
/// </summary>
public class _11001304 : NpcScript {
    internal _11001304(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005023$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:1228222807005745$ 
                // - I haven't been in $map:02000001$ for a long, long time. The air is... dustier than I remember. 
                return true;
            default:
                return true;
        }
    }
}
