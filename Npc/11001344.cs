using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001344: Jimmy
/// </summary>
public class _11001344 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005298$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005301$
                // - The impossible happened. Some prisoners escaped! No one has ever escaped from Alikar before! If I don't catch them, I'm through as an officer!
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
