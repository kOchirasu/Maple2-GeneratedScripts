using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001911: Battle Sim Researcher
/// </summary>
public class _11001911 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1115191007007385$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1115191007007388$
                // - Welcome to the $map:63000047$. How may I help you?
                switch (selection) {
                    // $script:1115191007007389$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        return 31;
                    // $script:1115191007007390$
                    // - You simulate battles here?
                    case 1:
                        return 32;
                    // $script:1115191007007391$
                    // - Who created all this?
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1115191007007392$
                // - The $map:63000047$ is home of the Chaotic Raid Battle Sim, where you can experience the most realistic virtual battles in Maple World. All the great heroes come here sooner or later.
                return 31;
            case (31, 1):
                // $script:1116121707007396$
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007397$
                    // - You simulate battles here?
                    case 0:
                        return 32;
                    // $script:1116121707007398$
                    // - Who created all this?
                    case 1:
                        return 33;
                    // $script:1116121707007399$
                    // - Thank you for your time.
                    case 2:
                        return 34;
                }
                return -1;
            case (32, 0):
                // $script:1115191007007393$
                // - The Chaotic Raid Battle Sim is a full-immersion virtual combat simulator that Dr. Gelimer created after decades of collecting combat data. You can use it to prepare for any kind of conflict situation.
                return 32;
            case (32, 1):
                // $script:1115191007007394$
                // - The simulations are so good, they're more dangerous than the real thing! On that note, you should definitely make sure you and your group are prepared before trying it out.
                return 32;
            case (32, 2):
                // $script:1116121707007400$
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007401$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        return 31;
                    // $script:1116121707007402$
                    // - Who created all this?
                    case 1:
                        return 33;
                    // $script:1116121707007403$
                    // - Thank you for your time.
                    case 2:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:1115191007007395$
                // - This place was created by my teacher, the great Dr. Gelimer. It is a masterpiece containing combat data taken from monsters throughout Maple World.
                return 33;
            case (33, 1):
                // $script:1116121707007404$
                // - Do you have any more questions? 
                switch (selection) {
                    // $script:1116121707007405$
                    // - Sell me on this $map:63000047$ business.
                    case 0:
                        return 31;
                    // $script:1116121707007406$
                    // - You simulate battles here?
                    case 1:
                        return 32;
                    // $script:1116121707007407$
                    // - Thank you for your time.
                    case 2:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1116121707007408$
                // - If you have any more questions, you know where to find me.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Next,
            (32, 2) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
