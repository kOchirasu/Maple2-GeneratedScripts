using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000514: Belma
/// </summary>
public class _11000514 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002195$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002199$
                // - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins.
                switch (selection) {
                    // $script:0831180407002200$
                    // - I'm here to make amends for my deeds.
                    case 0:
                        return 41;
                    // $script:0831180407002201$
                    // - I'm just a tourist!
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002202$
                // - All misdeeds must be punished. The punishment must fit the crime, or else we risk the criminal committing their crimes again.
                switch (selection) {
                    // $script:0831180407002203$
                    // - How can I reduce my sentence?
                    case 0:
                        return 43;
                }
                return -1;
            case (42, 0):
                // $script:0831180407002207$
                // - See the prisoners in here? Remember that you can always end up the same if you fail to heed the law.
                return 42;
            case (42, 1):
                // $script:0831180407002208$
                // - And that's the reason I have a tourist program here. You could learn a thing or two.
                return -1;
            case (43, 0):
                // $script:0831180407002204$
                // - How bold! You realize I don't issue pardons...
                switch (selection) {
                    // $script:0831180407002205$
                    // - I'll do anything. ANYTHING.
                    case 0:
                        return 44;
                }
                return -1;
            case (44, 0):
                // $script:0831180407002206$
                // - Will you, now? Hmm... I like the sound of that. In some cases, hard labor can substitute for time served. How about you pull the weeds in the prison yard? Do a good job, and I'll consider reducing your sentence.
                return -1;
            case (50, 0):
                // $script:1210061907004881$
                // - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins.
                switch (selection) {
                    // $script:1210061907004882$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004883$
                // - Who? You can't expect me to remember every rodent who comes in and out of $map:2000124$.
                switch (selection) {
                    // $script:1210061907004884$
                    // - Trust me, you'd remember this guy.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1210061907004885$
                // - <font color="#909090">(She listens begrudgingly as you describe $npcName:11001231[gender:0]$.)</font>
                //   As a matter of fact, I do remember him. There was something mysterious about the man.
                switch (selection) {
                    // $script:1210061907004886$
                    // - Do you know why he was here?
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1210061907004887$
                // - Only two kinds of people come to $map:2000124$: tourists and convicts. Since he's not rotting in one of our cells, I suppose he must have been a tourist.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.SelectableDistractor,
            (44, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
