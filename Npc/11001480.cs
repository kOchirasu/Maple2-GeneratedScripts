using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001480: Tara
/// </summary>
public class _11001480 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0106111607005767$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0106111607005768$
                // - Light and darkness... The war between the Lumarigons and the Kargons isn't over yet.
                //   All hope lies on $npcName:11001472[gender:1]$ recovering soon. She alone can save the Lumarigons.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
