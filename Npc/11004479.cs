using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004479: Meryl
/// </summary>
public class _11004479 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012196$
    // - Oh! You startled me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012197$
                // - Oh! You startled me.
                return 10;
            case (10, 1):
                // $script:1227192907012198$
                // - I'm here to study aetherine. We're really just scratching the surface when it comes to possible applications!
                switch (selection) {
                    // $script:1227192907012199$
                    // - What have you learned so far?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012200$
                // - Well, aetherine can make objects spontaneously levitate for almost no energy expenditure. I've measured the amount of aetherine in the floating buildings here, and there's very, very little.
                return 11;
            case (11, 1):
                // $script:1227192907012201$
                // - Our own levitation technology requires massive amounts of energy to work. If we can switch to aetherine, it will be a technological revolution!
                return 11;
            case (11, 2):
                // $script:1227192907012202$
                // - Of course, I don't know how any of it works. But I will. Oh yes, I will...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
