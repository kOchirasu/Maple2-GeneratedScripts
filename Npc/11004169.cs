using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004169: Mark
/// </summary>
public class _11004169 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010593$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010594$
                // - Guarding the armory is important work, but I'm glad Captain $npcName:11000119$ asked me to tag along.
                switch (selection) {
                    // $script:0806025707010595$
                    // - Are you on duty?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0806025707010596$
                // - Actually, I'm on leave at the moment. The captain asked me to be in his squad for Mushking Royale!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
