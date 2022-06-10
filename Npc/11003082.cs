using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003082: Chorrie
/// </summary>
public class _11003082 : NpcScript {
    internal _11003082(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0113143107007764$ 
                // - Sniff, sniff... Chorrie is scared... Too many evil people out there.
                return true;
            case 30:
                // $script:0113143107007767$ 
                // - No, no. Don't. I don't know anything. I really don't.
                switch (selection) {
                    // $script:0113143107007768$
                    // - Aww, it's okay. Take it easy.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0113143107007769$ 
                // - Sob... No one knows how I feel. Why can't I be left alone? Sob...
                return true;
            default:
                return true;
        }
    }
}
