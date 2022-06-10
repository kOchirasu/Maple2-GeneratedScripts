using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004256: Mysterious Medicine
/// </summary>
public class _11004256 : NpcScript {
    internal _11004256(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010972$ 
                // - <font color="#909090">(Pills and liquids in an assortment of colors lay scattered about.)</font> 
                return true;
            case 10:
                // $script:0829171107010973$ 
                // - <font color="#909090">(Pills and liquids in an assortment of colors lay scattered about.)</font> 
                // $script:0831140807011022$ 
                // - <font color="#909090">(A brief note can be found next to each item.)</font>
<font color="#ffd200">Cure-all Anesthetic Ver. 2</font>
Prevents blood clots, relieves fever and pain. Effective on muscle pain. Take up to 3 pills per day. Symptoms should abate within 2 days. 
                // $script:0831140807011023$ 
                // - <font color="#ffd200">Goldus Pharmaceutical's Digest+ Tab Ver. 5</font>
Aids with indigestion, loss of appetite, and overeating. Note for next test session: must be swallowed whole. DO NOT CHEW! Consume 3 times daily, with meals. Take for 3 full days for best results. 
                // $script:0831140807011024$ 
                // - <font color="#ffd200">Yellow Skin Goo (Name Pending)</font>
Minimizes appearance of eczema. Ointment should also treat folliculitis, boils, and acne, but the tests will tell for sure. Clean affect area, apply twice a day. Or, apply on a clean gauze and staple to skin. Wait, tape might be better. 
                // $script:0831140807011025$ 
                // - <font color="#ffd200">Ludi-solver (Experimental Solvent)</font>
Slows down or reverses the ludibrification process. NOT TO BE USED ON HUMANS. For inanimate object only. Ingredients extremely toxic. 
                return true;
            default:
                return true;
        }
    }
}
