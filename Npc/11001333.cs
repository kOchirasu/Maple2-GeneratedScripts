using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001333: Angelina
/// </summary>
public class _11001333 : NpcScript {
    internal _11001333(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005252$ 
                // - Sigh... May I help you?
                return true;
            case 30:
                // $script:1217012607005255$ 
                // - Judith is usually a good girl, but she can throw a tantrum like nobody's business. All because I refused to buy her a can of her favorite drink...
                return true;
            default:
                return true;
        }
    }
}
