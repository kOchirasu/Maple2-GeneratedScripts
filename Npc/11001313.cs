using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001313: Denden
/// </summary>
public class _11001313 : NpcScript {
    internal _11001313(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005032$ 
                // - What is it?
                return true;
            case 40:
                // $script:1227194507005676$ 
                // - Yeah? You never see a meerkat before?
                // $script:1227194507005677$ 
                // - I don't know what you want, but I'm not telling you anything unless <i>you</i> speak, first!
                switch (selection) {
                    // $script:1227194507005678$
                    // - Why does it matter who goes first?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227194507005679$ 
                // - It's one of the rules of Meerkat Patrol. So there!
                return true;
            default:
                return true;
        }
    }
}
