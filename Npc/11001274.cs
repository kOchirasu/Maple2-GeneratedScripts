using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001274: Madares
/// </summary>
public class _11001274 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1207123607004816$
    // - Barabung! Chochakka!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1207123607004819$
                // - Won't do it.
                switch (selection) {
                    // $script:1207123607004820$
                    // - What won't you do?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1207123607004821$
                // - No talk. Stranger danger.
                switch (selection) {
                    // $script:1207123607004822$
                    // - I'm not a stranger. I'm $MyPCName$.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1207123607004823$
                // - $MyPCName$ stranger! No talk.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
