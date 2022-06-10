using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004520: Mayo
/// </summary>
public class _11004520 : NpcScript {
    internal _11004520(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102174210002222$ 
                // - Non-stop service to $map:02020041$ in Kritias will be departing soon. 
                return true;
            case 10:
                // $script:0102174210002223$ 
                // - Non-stop service to $map:02020041$ in Kritias will be departing soon. 
                // $script:0102174210002224$ 
                // - Kritias is no place for pushovers. You know that, right? Well, if you're sure, hop aboard and I'll get you to $map:02020041$. 
                switch (selection) {
                    // $script:0102174210002225$
                    // - Take me to $map:02020041$!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0102174210002226$ functionID=1 
                // - All right. Away we go! 
                return true;
            default:
                return true;
        }
    }
}
