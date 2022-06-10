using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000181: Gilbert
/// </summary>
public class _11000181 : NpcScript {
    internal _11000181(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000750$ 
                // - What? 
                return true;
            case 40:
                // $script:0831180407000754$ 
                // - I've been working at this junkyard for over a decade, and this must be the strangest thing that has ever happened. 
                switch (selection) {
                    // $script:0831180407000755$
                    // - What is it?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407000756$ 
                // - A while back, a carriage full of junk came in with some Royal Guard weapons. I figured it must have been a mistake, so I checked with $npcName:11000171[gender:0]$. He said they were to be melted down, now that the court was canceled. 
                // $script:0831180407000757$ 
                // - If that were the case, the palace should've sent them to the forge instead of a junkyard. Right? 
                switch (selection) {
                    // $script:0831180407000758$
                    // - Yeah.
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0831180407000759$
                    // - Nah.
                    case 1:
                        Id = 43;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407000760$ 
                // - Right on. And I even saw $npcName:11000171[gender:0]$ sell the iron from the palace weapons to some dealer. How crazy do you have to be to steal from the palace?  
                return true;
            case 43:
                // $script:0831180407000761$ 
                // - Really? Huh. Maybe it's just me. 
                return true;
            default:
                return true;
        }
    }
}
