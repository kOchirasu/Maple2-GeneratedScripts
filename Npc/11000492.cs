using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000492: Nelph
/// </summary>
public class _11000492 : NpcScript {
    internal _11000492(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002158$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407002161$ 
                // - I've spoken with many people who are frustrated that the court will not be held. 
                switch (selection) {
                    // $script:0831180407002162$
                    // - It must be difficult to explain it to every single person.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002163$ 
                // - It certainly is, but I understand their frustration. They came all the way here to attend the court, only to have their plans ruined. They're upset and disappointed. 
                // $script:0831180407002164$ 
                // - Whatever the reason, I still feel personally responsible since I was the one charged with the preparations. 
                return true;
            case 40:
                // $script:0831180407002165$ 
                // - My job is to make sure $npcName:11000075[gender:1]$ and the other members of the royal family have everything they need for their day. I'm always busy, but I take pride in my position and my service to $map:02000025$. 
                return true;
            case 50:
                // $script:0831180407002166$ 
                // - Have you been to $map:02000076$? My mother lives there. I really should visit her, but I've been so busy that I haven't had the time since preparations began.  
                // $script:0831180407002167$ 
                // - Once my work here is done and I've sorted out all the issues, I'll go and visit her first thing! I've been sending her letters, it's just... she can't see. A disease took her eyesight. Sigh...  
                return true;
            default:
                return true;
        }
    }
}
