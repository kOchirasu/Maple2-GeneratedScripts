using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003247: Joddy
/// </summary>
public class _11003247 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0403155707008154$
    // - $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008157$
                // - Long time, no see. You did great, as usual.
                return -1;
            case (40, 0):
                // $script:0403155707008158$
                // - I'm no hero like you, but I'm sure trying!
                switch (selection) {
                    // $script:0403155707008159$
                    // - Where are you headed?
                    case 0:
                        return 41;
                    // $script:0403155707008160$
                    // - I hope there are no dogs or mushrooms this time.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0403155707008161$
                // - $map:02000087$. It's not far from $map:02000001$. The people there need help, and I'm going to do my best to give it to them.
                return -1;
            case (42, 0):
                // $script:0403155707008162$
                // - C'mon! I'm not afraid of dogs or mushrooms anymore. I'm a real guard, almost!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
