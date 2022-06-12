using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001166: Merin
/// </summary>
public class _11001166 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1008163207004068$
    // - What should I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1008163207004071$
                // - Shh! Please, keep your voice down! <i>That mage</i> can't know I'm here!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
