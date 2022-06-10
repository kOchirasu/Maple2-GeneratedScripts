using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001911: Battle Sim Researcher
/// </summary>
public class _11001911 : NpcScript {
    internal _11001911(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1115191007007385$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:1115191007007388$ 
                // - Welcome to the $map:63000047$. How may I help you?
                switch (selection) {
                    // $script:1115191007007389$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1115191007007390$
                    // - You simulate battles here?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1115191007007391$
                    // - Who created all this?
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1115191007007392$ 
                // - The $map:63000047$ is home of the Chaotic Raid Battle Sim, where you can experience the most realistic virtual battles in Maple World. All the great heroes come here sooner or later.
                // $script:1116121707007396$ 
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007397$
                    // - You simulate battles here?
                    case 0:
                        Id = 32;
                        return false;
                    // $script:1116121707007398$
                    // - Who created all this?
                    case 1:
                        Id = 33;
                        return false;
                    // $script:1116121707007399$
                    // - Thank you for your time.
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            case 32:
                // $script:1115191007007393$ 
                // - The Chaotic Raid Battle Sim is a full-immersion virtual combat simulator that Dr. Gelimer created after decades of collecting combat data. You can use it to prepare for any kind of conflict situation.
                // $script:1115191007007394$ 
                // - The simulations are so good, they're more dangerous than the real thing! On that note, you should definitely make sure you and your group are prepared before trying it out.
                // $script:1116121707007400$ 
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007401$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1116121707007402$
                    // - Who created all this?
                    case 1:
                        Id = 33;
                        return false;
                    // $script:1116121707007403$
                    // - Thank you for your time.
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:1115191007007395$ 
                // - This place was created by my teacher, the great Dr. Gelimer. It is a masterpiece containing combat data taken from monsters throughout Maple World.
                // $script:1116121707007404$ 
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007405$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1116121707007406$
                    // - You simulate battles here?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1116121707007407$
                    // - Thank you for your time.
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1116121707007408$ 
                // - If you have any more questions, you know where to find me.
                return true;
            default:
                return true;
        }
    }
}
