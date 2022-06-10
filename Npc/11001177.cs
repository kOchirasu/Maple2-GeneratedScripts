using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001177: Gomei
/// </summary>
public class _11001177 : NpcScript {
    internal _11001177(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1012113807004092$ 
                // - Nothing to report, $male:sir,female:ma'am$.
                return true;
            case 30:
                // $script:1012113807004095$ 
                // - I'm fairly new to the Green Hoods, but I've been stationed here long enough to get the lay of the land. If something happens in $map:02000057$, I'll be the first to know. But, ah, let me know if you see anything suspicious anyway.
                switch (selection) {
                    // $script:1012113807004096$
                    // - How do you like being a member of the militia?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1012113807004097$ 
                // - Well, I've learned a lot of things. Like how being a guard means learning how to think on your feet. I'm not so great at that now, but I try hard.
                return true;
            default:
                return true;
        }
    }
}
