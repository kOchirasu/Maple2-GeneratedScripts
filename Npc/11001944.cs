using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001944: Guitar Student
/// </summary>
public class _11001944 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1123165007007490$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208184307007530$
                // - I hear there's a lot of top talent here for the audition. I'm a little worried...
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
