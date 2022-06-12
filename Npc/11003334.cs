using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003334: Ralph
/// </summary>
public class _11003334 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0426090007008448$
    // - Who's behind this mess?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0426090007008451$
                // - You! What are <i>you</i> doing here?!
                switch (selection) {
                    // $script:0426090007008452$
                    // - Good to see you, too.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0426090007008453$
                // - I gave you what you wanted. Why are you bugging me?
                switch (selection) {
                    // $script:0426090007008454$
                    // - Did a blond man run through here?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0426090007008455$
                // - Yeah. He was headed for $map:02000138$. Now leave me alone!
                switch (selection) {
                    // $script:0426090007008456$
                    // - I'll see you later.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0426090007008457$
                // - Why would I ever want to see you again?!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
