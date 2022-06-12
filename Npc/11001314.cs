using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001314: Temorro
/// </summary>
public class _11001314 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005033$
    // - I've answered plenty of your questions already.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005683$
                // - I'm sick of the constant questions! Even if I told them the answers, they wouldn't remember them, the dopes!
                switch (selection) {
                    // $script:1227194507005684$
                    // - It sounds like you don't actually know the answers.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227194507005685$
                // - Why you! It'll take more than that to shake their faith in me. Do I look like an easy mark to you?
                switch (selection) {
                    // $script:1227194507005686$
                    // - No.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1227194507005687$
                // - Maybe you don't know how this works, but you're supposed to trade intel with me, not question my credibility. Well, forget you!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
