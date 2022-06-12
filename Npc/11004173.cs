using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004173: Tara
/// </summary>
public class _11004173 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010608$
    // - Mm?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010609$
                // - Sorry, I've already got a squad. See? There's the guy selling churros, the girl strutting around over there, and that guy shooting finger-guns.  I couldn't ask for better teammates.
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
